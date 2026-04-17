from datetime import datetime

def generate_report(audit_results, parsed_logs, device):
    total_logs = len(parsed_logs)
    auth_failures = sum(1 for log in parsed_logs if log['category'] == 'authentication_failure')
    rate_limits = sum(1 for log in parsed_logs if log['category'] == 'rate_limit_exceeded')
    connection_events = sum(1 for log in parsed_logs if log['category'] == 'connection_event')
    successful_logins = sum(1 for log in parsed_logs if log['category'] == 'successful_login')


    checks = ""
    for check, result in audit_results.items():
       checks += f"<p>{check}: {result}</p>"


    html = f"""
    <html>
    <body>
       <h1>Network Audit Report</h1>
       <p>Device: {device['hostname']}</p>
        {checks}

       <h2>Log Analysis</h2>
       <p>Total Events: {total_logs}</p>
       <p>Authentication Failures: {auth_failures}</p>
       <p>Rate Limits Exceeded: {rate_limits}</p>
       <p>Connection Events: {connection_events}</p>
       <p>Successful Logins: {successful_logins}</p>


       
    </body>
    </html>
    """
   

    with open('reports/report.html', 'w') as file:
        file.write(html)
    return html    
   