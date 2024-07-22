import requests

#urls =["https://shantanuuchak.tech","https://quastech.in","https://innovaccer.com/contact-us","https://www.infogain.com/about/contact-us/"]
#res = requests.get(""https://website.com")

def split_quote(text):
  return text.split('"')


def remove_mailto(email_str):
  return email_str.replace("mailto:","")


def extract_mail(data_list):
  email= []
  for i in data_list:
    if "@" in i and "."in i and not "/" in i:
      email.append(remove_mailto(i))
  return email

def fetch(url):
  res = requests.get(url)

  if res.status_code == 200:
    return res.text

  print(f"failed with error code: {res.status_code}")
  return ""

urls = []

while True:
  user_input = input("Enter a url or N to exit:")
  if user_input == "N":
    print("url list is ready")
    break
  if "://" not in user_input:
    print("Enter a valid url")
  else:
    urls.append(user_input)

email = []

for url in urls:
  data = fetch(url)
  data_list = split_quote(data)
  mail_list = extract_mail(data_list)
  email.extend(mail_list)

#print(emails)


#unique_emails = []                    
#for mail in emails:                     
#   unique_emails.append(mail)

#print(unique_emails)

unique_emails = set(email)  
print(unique_emails)


#write output to a file
f = open("emails.txt","w")
f.write(str(unique_emails))
f.close()


    