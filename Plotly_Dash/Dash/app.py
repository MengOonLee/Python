import os
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
        elem['UnitPrice'] = round(
            float(elem['UnitPrice'].strip()), 2)
        elem['InvoiceDate'] = datetime.datetime.strptime(
            elem['InvoiceDate'].strip(), '%m/%d/%Y %H:%M')
        elem['OrderValue'] = round(
            elem['Quantity']*elem['UnitPrice'], 2)
        elem['YearMonth'] = elem['InvoiceDate']\
            .strftime('%Y-%m')
        yield elem
        
class TopSalesCountryFn(beam.CombineFn):
    def create_accumulator(self):
        country, sales = None, 0.0
        return country, sales
    
    def add_input(self, accumulator, elem):
        country, sales = accumulator
        if elem['TotalSales'] > sales:
            accumulator = (elem['Country'], elem['TotalSales'])
        return accumulator
    
    def merge_accumulators(self, accumulators):
        return accumulators[0]
    
    def extract_output(self, accumulator):
        country, sales = accumulator
        return {'Country':country, 'TotalSales':sales}

with beam.Pipeline(
    runner=InteractiveRunner()
) as pipeline:
    
    sales = pipeline \
        | ReadCsvFiles(csv_files) \
        | beam.ParDo(ParseSales())
    
    sales_line = sales \
        | beam.Map(lambda x: beam.Row(**x)) \
        | 'line' >> beam.GroupBy('YearMonth')\
            .aggregate_field('OrderValue', sum, 'TotalSales') \
        | beam.Map(lambda x: x._asdict()) \
        | beam.Map(lambda x: {
            'YearMonth':str(x['YearMonth']),
            'TotalSales':round(float(x['TotalSales']), 2)})
    df_line = ib.collect(sales_line)
    fig_line = px.line(data_frame=df_line,
        x='YearMonth', y='TotalSales',
        title='Total Sales by Month')
    
    sales_bar = sales \
        | beam.Map(lambda x: beam.Row(**x)) \
        | 'bar' >> beam.GroupBy('Country')\
            .aggregate_field('OrderValue', sum, 'TotalSales') \
        | beam.Map(lambda x: x._asdict()) \
        | beam.Map(lambda x: {
            'Country':str(x['Country']),
            'TotalSales':round(float(x['TotalSales']), 2)})
    df_bar = ib.collect(sales_bar)
    fig_bar = px.bar(data_frame=df_bar,
        x='TotalSales', y='Country',
        orientation='h',
        title='Total Sales by Country')

    top_sales_country = sales_bar \
        | beam.CombineGlobally(TopSalesCountryFn())
    max_country = ib.collect(top_sales_country)\
        ['Country'][0]
    
# Create the Dash app
app = dash.Dash(__name__)

# Create the dash layout and overall div
app.layout = dash.html.Div(children=[
    # Add a H1
    dash.html.H1('Sales Figures'), 
    # Add a div containing the line figure
    dash.html.Div(dash.dcc.Graph(id='fig_line',
        figure=fig_line)), 
    # Add a div containing the bar figure
    dash.html.Div(dash.dcc.Graph(id='fig_bar',
        figure=fig_bar)), 
    # Add the H3
    dash.html.H3(f'The largest country by sales was \
        {max_country}')
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
