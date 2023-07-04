import logging
logging.getLogger().setLevel(logging.INFO)
import csv
import codecs
import datetime
import dash
import plotly.express as px
import apache_beam as beam
import apache_beam.runners.interactive.interactive_beam as ib
from apache_beam.runners.interactive.interactive_runner \
    import InteractiveRunner

csv_files = ['./data/ecom_sales.csv']

@beam.ptransform_fn
def ReadCsvFiles(pbegin: beam.pvalue.PBegin, file_patterns):
        
    def expand_pattern(pattern):
        for m in beam.io.filesystems.FileSystems.match([
                pattern])[0].metadata_list:
            yield m.path

    def read_csv_lines(file):
        with beam.io.filesystems.FileSystems.open(file) as f:
            for row in csv.DictReader(
                    codecs.iterdecode(f, 'utf-8')):
                yield dict(row)
        
    return pbegin \
        | beam.Create(file_patterns) \
        | beam.FlatMap(expand_pattern) \
        | beam.FlatMap(read_csv_lines)

class ParseSales(beam.DoFn):
    def process(self, elem):
        elem['Quantity'] = int(elem['Quantity'].strip())
        elem['UnitPrice'] = round(float(
            elem['UnitPrice'].strip()), 2)
        elem['InvoiceDate'] = datetime.datetime.strptime(
            elem['InvoiceDate'].strip(), '%m/%d/%Y %H:%M')
        elem['OrderValue'] = round(
            elem['Quantity'] * elem['UnitPrice'], 2)
        elem['YearMonth'] = elem['InvoiceDate'].strftime('%Y-%m')
        yield elem

with beam.Pipeline(
    runner=InteractiveRunner()
) as pipeline:
    
    country_list = ['United Kingdom', 'Germany', 'France',
        'Australia', 'Hong Kong']
    
    sales = pipeline \
        | ReadCsvFiles(csv_files) \
        | beam.Filter(lambda x: x['Country'] in country_list) \
        | beam.ParDo(ParseSales())
    
    sales_line = sales \
        | beam.Map(lambda x: beam.Row(**x)) \
        | beam.GroupBy('YearMonth', 'Country')\
            .aggregate_field('OrderValue', sum, 'TotalSales') \
        | beam.Map(lambda x: x._asdict()) \
        | beam.Map(lambda x: {
            'YearMonth':str(x['YearMonth']),
            'Country':str(x['Country']),
            'TotalSales':round(float(x['TotalSales']), 2)})
    df_line = ib.collect(sales_line)
    fig_line = px.line(data_frame=df_line,
        x='YearMonth', y='TotalSales', color='Country',
        title='Total Sales by Month')

# Create the Dash app
app = dash.Dash(__name__)

# Set up the layout with a single graph
app.layout = dash.dcc.Graph(
  id='fig_line',
  # Insert the line graph
  figure=fig_line)

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
