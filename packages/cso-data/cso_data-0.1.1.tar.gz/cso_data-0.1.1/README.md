# cso_app

## Install
Simply use the following pip command
~~~
pip install cso-data
~~~

## How to
* Simply import the CSO_df class and call its method get_cso_table. 
~~~
# import class
from cso_data import CSO_df

# request table
df = CSO_df().get_cso_table('HPA02')
~~~
This method takes one input which is a table code which can be found on https://data.cso.ie/ . 
This returns a dataframe of the table of the data you request

See cso_example.ipynb
