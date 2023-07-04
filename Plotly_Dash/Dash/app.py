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

logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'
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
    
    country_list = ['EIRE', 'Netherlands', 'Germany', 'France',
        'Australia']
    
    sales = pipeline \
        | ReadCsvFiles(csv_files) \
        | beam.Filter(lambda x: x['Country'] in country_list) \
        | beam.ParDo(ParseSales())
    
    sales_bar = sales \
        | beam.Map(lambda x: beam.Row(**x)) \
        | beam.GroupBy('Country')\
            .aggregate_field('OrderValue', sum, 'TotalSales') \
        | beam.Map(lambda x: x._asdict()) \
        | beam.Map(lambda x: {
            'Country':str(x['Country']),
            'TotalSales': round(float(x['TotalSales']), 2)})
    df_bar = ib.collect(sales_bar)
    fig_bar = px.bar(data_frame=df_bar,
        x='TotalSales', y='Country', color='Country',
        color_discrete_map={'EIRE':'lightblue',
            'Germany':'orange', 'France':'darkblue', 
            'Australia':'green', 'Netherlands':'red'})
    
    top_sales_country = sales_bar \
        | beam.CombineGlobally(TopSalesCountryFn())
    top_country = ib.collect(top_sales_country)['Country'][0]

app = dash.Dash(__name__)

app.layout = dash.html.Div(children=[
    # Add the company logo
    dash.html.Img(src=logo_link),
    dash.html.H1('Sales by Country'),
    dash.html.Div(dash.dcc.Graph(figure=fig_bar), 
        style={'width':'750px', 'margin':'auto'}),
    # Add an overall text-containing component
    dash.html.Span(children=[
        # Add the top country text
        'This year, the most sales came from: ', 
        dash.html.B(top_country),
        # Italicize copyright notice
        dash.html.I(' Copyright E-Com INC')])
], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
