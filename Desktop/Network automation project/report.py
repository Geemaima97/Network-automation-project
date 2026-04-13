from datetime import datetime

def generate_report(audit_results,device):
    checks = ""
    for check, result in audit_results.items():
       checks += f"<p>{check}: {result}</p>"

    html = f"""
    <html>
    <body>
       <h1>Network Audit Report</h1>
       <p>Device: {device['hostname']}</p>
       {checks}
    </body>
    </html>
    """
   

    with open('reports/report.html', 'w') as file:
        file.write(html)
    return html    
   