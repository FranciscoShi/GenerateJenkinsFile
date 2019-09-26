
defaultTemp: str = """
pipeline{
    agent{ label {  {{ nodename }} }}

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages{
        {% for stg in stages %}
        stage({{ stg.stage_name }}){
            steps{
                timeout(time: {{ stg.timeout_time }} , unit: {{ stg.timeout_unit }}){
                    script{
                        {{ stg.scripts }}
                    }
                }
            }
        }
        {% endfor %}
    }
}

"""
