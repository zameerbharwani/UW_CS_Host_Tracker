from tabulate import tabulate

class HTMLGenerator:

    @staticmethod
    def generateHeader():
        return """ 
        <!DOCTYPE html>
                <html>
                    <head>
		        <style>
			    footer {
	  		        text-align: center;
		    		padding: 3px;
				color: #A9A9A9;
				position: fixed;
				left: 0;
				bottom: 0;
				width: 100%;
			    }
		    </style>
	        </head>
        """
    @staticmethod
    def generateStaticBody(machineSpecs):
        return f"""
                    <body>
		        <h1> UWaterloo CS Machine Status </h1>
                        {tabulate(machineSpecs, headers='firstrow', tablefmt='html')}
                """
    @staticmethod
    def generateDynamicBody(machineData, updateTime):
        return f"""
                  {tabulate(machineData, headers='firstrow', tablefmt='html')}
                  <footer>
			    <p>Author: Zameer Bharwani</p>
		        </footer>
	            </body>
                </html>
              """
