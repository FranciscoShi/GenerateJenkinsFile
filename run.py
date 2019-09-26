from jinja2 import Template
from templates.template import *


template = Template(defaultTemp)


builders = 'sh " echo hello "'
stages = [{"stage_name": "'build'", "timeout_time": "10", "timeout_unit": "'MINUTES'", "scripts": builders},
          {"stage_name": "'unitTest'", "timeout_time": "10", "timeout_unit": "'MINUTES'", "scripts": builders}]


print(template.render(nodename="'node01'", stages=stages))
