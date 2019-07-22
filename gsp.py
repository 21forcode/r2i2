import gspread
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from PIL import Image
import pytesseract
def crop(image_path, coords, saved_location):
	image_obj = Image.open('/home/lucky21/Music/work/img2.jpg')
	#coords=(311,448,680,690)
	#print(image_obj.size)
	im3 = image_obj.resize((800,1079), Image.BILINEAR)
	cropped_image = im3.crop(coords)
	#cropped_image.save(saved_location)
	cropped_image.show()
	#conductng ocr on cropped image
	p=pytesseract.image_to_string(cropped_image,lang='eng',config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/ -psm 6")
	s=p.split('\n')

	for item in s:
		if item == '':
			s.remove(item)
	l= len(s);
	#or i in range (l-1):
	return (s[l-1])
if __name__ == '__main__':
	image = '/home/lucky21/Music/work/img2.jpg'
	scope = ['https://spreadsheets.google.com/feeds',
        	  'https://www.googleapis.com/auth/drive']
	#check for the credentials of google spreadsheet api
	credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/lucky21/Downloads/manish for R2i2-670ce6e648db.json', scope)
	gc = gspread.authorize(credentials)
	sh=gc.open("project").sheet1
	#takes the input of path of the image to be extracted
	#f = raw_input("Enter the name of your text file - please use / backslash when typing in directory path: ")
	#Returns the result of a Tesseract OCR run on the image to string in english and hindi 
	p=pytesseract.image_to_string(Image.open(image),lang='eng',config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/ -psm 6")
	#dump the extracted data to google -spreadsheet API
	s=p.split('\n')
	i=0
	for item in s:
	#remove the empty lines 
		if not item:
			s.remove(item)
	#dump the ocr data into spreadsheet
	i=1
	for item in s:
		sh.update_cell(i,1,item)
		i=i+1
	print(sh.get_all_values)
	#create another spreadsheet to store ocr data in organised manner
	osh=gc.open("organize").sheet1
	osh.update_cell(1,1,'Name')
	osh.update_cell(3,1,'DOB')
	osh.update_cell(5,1,'Birth Place')
	sname=crop(image, (311,652,448,690), 'cropped.jpg')
	osh.update_cell(1,3,sname)
	name=crop(image, (311,697,508,732), 'cropped.jpg')
	osh.update_cell(1,2,name)
	dob=crop(image, (593,715,783,782), 'cropped.jpg')
	osh.update_cell(3,2,dob)
	pob=crop(image, (353,786,688,822), 'cropped.jpg')
	osh.update_cell(5,2,pob)
	#print all the records of spreadsheet
	for item in osh.get_all_values():
	
		print(item)

	
	
