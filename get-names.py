import pdfplumber
import enchant



PATH = '/Users/kayleemolin/Desktop/psych-11.pdf'

   
def get_text(path):
   with pdfplumber.open(path) as pdf:
      print(len(pdf.pages)) 
      text = ''
      for page in pdf.pages:
         if page.extract_text() is not None:
            page_text = page.extract_text()
            text = text + page_text
   return text 



#print(get_text(PATH))

def main():
   text = get_text(PATH)
   text_list = text.split()
   
   caps = []
   
   for word in text_list:
      if len(word) >= 2 and word[0].isupper():
         caps.append(word)
   
   my_dict = {i:caps.count(i) for i in caps}
   for item in my_dict:
      print(item)
         
main()