import re
import nltk


TIMESTAMP_PATTERN = r'\w+\s+\d+\s[\d:.]+\s\w+'
SEVERITY_PATTERN = r'-(\d)-'
MNEMONIC_PATTERN = r'-\d-(\w+)'
MESSAGE_PATTERN = r'\s:\s(.+)'

def classify_message(message):
    tokens = nltk.word_tokenize(message.lower())
    if 'permission' in tokens or 'denied' in tokens or 'pam' in tokens or 'failed' in tokens:
        return 'authentication_failure'
    
    if 'rate' in tokens or 'limit' in tokens:
        return 'rate_limit_exceeded'
    
    if 'connection' in tokens or 'closed' in tokens:
        return 'connection_event'
    
    if 'accepted'in tokens:
        return 'successful_login' 
    
    return 'unknown' 

def parse_logs(log_data):
    parsed_logs = []
    for line in log_data.splitlines():
       timestamp_match = re.search(TIMESTAMP_PATTERN, line)
       severity_match  = re.search(SEVERITY_PATTERN, line)
       mnemonic_match  = re.search(MNEMONIC_PATTERN, line)
       message_match   = re.search(MESSAGE_PATTERN, line)



       if timestamp_match and severity_match and mnemonic_match and message_match:
            timestamp = timestamp_match.group()
            severity = severity_match.group(1)
            mnemonic = mnemonic_match.group(1)
            message = message_match.group(1) 
            category = classify_message(message.lower())

            parsed_entry = {
                "timestamp": timestamp,
                "severity": severity,
                "mnemonic": mnemonic,
                "message": message,
                "category": category

            }
            parsed_logs.append(parsed_entry)


    return parsed_logs

if __name__ == "__main__":
    with open('sample_logs.txt', 'r') as f:
        log_data = f.read()
    results = parse_logs(log_data)
    for entry in results[:20]:
      print(entry)
