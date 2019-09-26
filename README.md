# GenerateJenkinsFile
模板生成Jenkinsfile


```python

python3 run.py

```


```
pipeline{
    agent{ label {  'node01' }}

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages{

        stage('build'){
            steps{
                timeout(time: 10 , unit: 'MINUTES'){
                    script{
                        sh " echo hello "
                    }
                }
            }
        }

        stage('unitTest'){
            steps{
                timeout(time: 10 , unit: 'MINUTES'){
                    script{
                        sh " echo hello "
                    }
                }
            }
        }

    }
}

```
