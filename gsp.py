#import needed modules
import gspread
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
#check for the credentials of google spreadsheet api
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/lucky21/Downloads/manish for R2i2-670ce6e648db.json', scope)
gc = gspread.authorize(credentials)
#create a spreadsheet

sh=gc.open("project").sheet1
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
f =""
#takes the input of path of the image to be extracted
f = raw_input("Enter the name of your text file - please use / backslash when typing in directory path: ")
#Returns the result of a Tesseract OCR run on the image to string in english and hindi 
p=pytesseract.image_to_string(Image.open(f),lang='eng+hin',config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/ -psm 6")
#dump the extracted data to google -spreadsheet API
s=p.split('\n')
i=0
for item in s:
#remove the empty lines 
	if not item:
		s.remove(item)
#dump the ocr data into spreadsheet
for item in s:
	i=i+1
	sh.update_cell(i,1,item)
#print all the records of spreadsheet
print(sh.get_all_values())
#create another spreadsheet to store ocr data in organised manner
osh=gc.open("organize").sheet1
#update the first row with attributes name
osh.update_cell(1,1,'Name')
osh.update_cell(2,1,'Address')
osh.update_cell(3,1,'DOB')

#append name address and date of birth in respective columns
for item in s:
	p=item.find('Name',0,5)
	if p == 0:
		#print(item[4:])
		osh.update_cell(1,2,item[4:])
	if item.find('Add',0,5) == 0:
		#print(item[3:])
		osh.update_cell(2,2,item[3:])
	if item.find('DOB') >= 0:
		osh.update_cell(3,2,item[(item.find('DOB'))+3:])
		#print(item[(item.find('DOB'))+3:])
#print all the records of spreadsheet
for item in osh.get_all_values():

	print(item)
