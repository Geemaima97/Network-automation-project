from openai import OpenAI
from configuration import OPENAI_API_KEY


def analyze_logs(parsed_logs, device):
    
    total_logs = len(parsed_logs)
    auth_failures = sum(1 for log in parsed_logs if log['category'] == 'authentication_failure')
    rate_limits = sum(1 for log in parsed_logs if log['category'] == 'rate_limit_exceeded')
    connection_events = sum(1 for log in parsed_logs if log['category'] == 'connection_event')
    successful_logins = sum(1 for log in parsed_logs if log['category'] == 'successful_login')  

    prompt = f"""Analyze the network security posture based on the following log summary for device {device['hostname']} Provide a brief analysis of potential security issues and recommendations for improvement.:  

    Total Logs: {total_logs}
    Authentication Failures: {auth_failures}
    Rate Limits Exceeded: {rate_limits}
    Connection Events: {connection_events}      
    Successful Logins: {successful_logins}
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Analyze the network security posture based on the provided log summary."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300

    )
    return response.choices[0].message.content