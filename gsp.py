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
gc.create('project')

sh=gc.open("project").sheet1
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#Returns the result of a Tesseract OCR run on the image to string in english and hindi 
p=pytesseract.image_to_string(Image.open('/home/lucky21/Downloads/img7.png'),lang='eng+hin',config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/ -psm 6")
#dump the extracted data to google -spreadsheet API
s=p.split('\n')
i=0
for item in s:
	
	if not item:
		s.remove(item)
for item in s:
	i=i+1
	sh.update_cell(i,1,item)
print(sh.get_all_values())


