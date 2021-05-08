from tabulate import tabulate
import os


#TODO: separate static static and dynamic code

class HTMLGenerator:
    start_pos = 0
    @staticmethod
    def generatePage(machineSpecs, machineData, meanTime):
        if os.path.exists('index.html'):
            os.remove('index.html')
        index_html = open('index.html','w+')
        index_html.write(f""" 
        <!DOCTYPE html>
                <html>
                    <head>
		        <style>
			    footer {{
	  		        text-align: center;
		    		padding: 3px;
				color: #A9A9A9;
				position: fixed;
				left: 0;
				bottom: 0;
				width: 100%;
			    }}
		    </style>
	        </head>
            <body>
		        <h1> UWaterloo CS Machine Status </h1>
                        {tabulate(machineSpecs, headers='firstrow', tablefmt='html')}
                        {tabulate(machineData, headers='firstrow', tablefmt='html')}
                    <p style="color:grey;"> Updated @: {meanTime}</p>
                <img src="users_vs_time.png" alt="# of users" style="width:750px;height:500px;">
                <img src="load_vs_time.png" alt="load average" style="width:750px;height:500px;">
                  <footer>
			    <p>Author: Zameer Bharwani</p>
		        </footer>
	            </body>
                </html>

        """)
        index_html.close()
