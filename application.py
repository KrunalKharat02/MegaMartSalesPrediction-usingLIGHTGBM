import pickle
from flask import Flask, request
from flask import Flask, render_template, request
from fpdf import FPDF

# load model
with open("model_pickle","rb") as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
def create_pdf(Item_Type,Item_MRP,Outlet_Type,Outlet_Size,Outlet_Location_Type,Outlet_Establishment_year
                   ,Outlet_Identifier,result):
    # Create a new PDF object
    pdf = FPDF()
    pdf.add_page()

    # Add text to the PDF using the form data
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Mega Mart Sales Prediction', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Item Type: {Item_Type}', 0, 1)
    pdf.cell(0, 10, f'Item MRP: {Item_MRP}', 0, 1)
    pdf.cell(0, 10, f'Outlet Type: {Outlet_Type}', 0, 1)
    pdf.cell(0, 10, f'Oulet Size: {Outlet_Size}', 0, 1)
    pdf.cell(0, 10, f'Outlet Location Type: {Outlet_Location_Type}', 0, 1)
    pdf.cell(0, 10, f'Outlet Establishment year: {Outlet_Establishment_year}', 0, 1)
    pdf.cell(0, 10, f'Outlet Identifier: {Outlet_Identifier}', 0, 1)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f'Prediction(in rupee): {round(result,3)}', 0, 1)

    # Save the PDF to the server's file system
    pdf_path = './static/response.pdf'
    pdf.output(pdf_path, 'F')

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/about', methods = ['GET'])
def about():
    return render_template("about.html")

@app.route('/analysis', methods = ['GET'])
def analysis():
    
    return render_template("analysis.html")

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template("contact.html")

@app.route('/predict', methods = ['GET','POST'])
def predict():

    if(request.method == 'POST'):
        data = request.form
        Item_Type = data["Item_Type"]
        Item_MRP = int(data["Item_MRP"])
        Outlet_Type = data["Outlet_Type"]
        Outlet_Size = data["Outlet_Size"]
        Outlet_Location_Type=data["Outlet_Location_Type"]
        Outlet_Establishment_year = data["Outlet_Establishment_Year"]
        Outlet_Identifier= data["Outlet_Identifier"]
        
        #Item_MRP
        if (Item_MRP >= 20 and Item_MRP < 75):
            Item_MRP_a = 1
            Item_MRP_b = 0
            Item_MRP_c = 0
            Item_MRP_d = 0
        elif (Item_MRP >= 75 and Item_MRP < 140):
            Item_MRP_a = 0
            Item_MRP_b = 1
            Item_MRP_c = 0
            Item_MRP_d = 0
        elif (Item_MRP >= 140 and Item_MRP < 205):
            Item_MRP_a = 1
            Item_MRP_b = 0
            Item_MRP_c = 1
            Item_MRP_d = 0
        else:
            Item_MRP_a = 0
            Item_MRP_b = 0
            Item_MRP_c = 0
            Item_MRP_d = 1

        #Outlet Type
        if Outlet_Type =="Grocery Store":
            Outlet_Type_Grocery_Store = 1
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 0
        elif Outlet_Type =="Supermarket Type1":
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 1
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 0
        elif Outlet_Type=="Supermarket Type2":
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 1
            Outlet_Type_Supermarket_Type3 = 0
        else:
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 1

        #Outlet_size
        if Outlet_Size=="High":
            Outlet_Size_High = 1       
            Outlet_Size_Medium = 0               
            Outlet_Size_Small = 0
        elif Outlet_Size=="Medium":
            Outlet_Size_High = 0      
            Outlet_Size_Medium = 1               
            Outlet_Size_Small = 0
        else:
            Outlet_Size_High = 0       
            Outlet_Size_Medium = 0               
            Outlet_Size_Small = 1

        #Outlet Location Type
        if Outlet_Location_Type=="Tier 1":
            Outlet_Location_Type_Tier1 = 1
            Outlet_Location_Type_Tier2 = 0
            Outlet_Location_Type_Tier3 = 0
            
        elif Outlet_Location_Type=="Tier 2":
            Outlet_Location_Type_Tier1 = 0
            Outlet_Location_Type_Tier2 = 1
            Outlet_Location_Type_Tier3 = 0
        else:
            Outlet_Location_Type_Tier1 = 0
            Outlet_Location_Type_Tier2 = 0
            Outlet_Location_Type_Tier3 = 1

        # Outlet_Establishment_year
        Outlet_Establishment_Year_1985 = 0
        Outlet_Establishment_Year_1987 = 0
        Outlet_Establishment_Year_1997 = 0
        Outlet_Establishment_Year_1998 = 0
        Outlet_Establishment_Year_1999 = 0
        Outlet_Establishment_Year_2002 = 0
        Outlet_Establishment_Year_2004 = 0
        Outlet_Establishment_Year_2007 = 0
        Outlet_Establishment_Year_2009 = 0

        if Outlet_Establishment_year == 1985:
            Outlet_Establishment_Year_1985 = 1
        elif Outlet_Establishment_year == 1987:
            Outlet_Establishment_Year_1987 = 1
        elif Outlet_Establishment_year == 1997:
            Outlet_Establishment_Year_1997 = 1
        elif Outlet_Establishment_year == 1998:
            Outlet_Establishment_Year_1998 = 1
        elif Outlet_Establishment_year == 1999:
            Outlet_Establishment_Year_1999 = 1
        elif Outlet_Establishment_year == 2002:
            Outlet_Establishment_Year_2002 = 1
        elif Outlet_Establishment_year == 2004:
            Outlet_Establishment_Year_2004 = 1
        elif Outlet_Establishment_year == 2007:
            Outlet_Establishment_Year_2007 = 1
        else :
            Outlet_Establishment_Year_2009 = 1
        
        # Outlet_Identifier
        Outlet_Identifier_OUT010 = 0
        Outlet_Identifier_OUT013 = 0
        Outlet_Identifier_OUT017 = 0
        Outlet_Identifier_OUT018 = 0
        Outlet_Identifier_OUT019 = 0
        Outlet_Identifier_OUT027 = 0
        Outlet_Identifier_OUT035 = 0
        Outlet_Identifier_OUT045 = 0
        Outlet_Identifier_OUT046 = 0
        Outlet_Identifier_OUT049 = 0
        
        if Outlet_Identifier == "OUT010":
            Outlet_Identifier_OUT010 = 1
        elif Outlet_Identifier == "OUT013":
            Outlet_Identifier_OUT013 = 1
        elif Outlet_Identifier == "OUT017":
            Outlet_Identifier_OUT017 = 1
        elif Outlet_Identifier == "OUT018":
            Outlet_Identifier_OUT018 = 1
        elif Outlet_Identifier == "OUT019":
            Outlet_Identifier_OUT019 = 1
        elif Outlet_Identifier == "OUT027":
            Outlet_Identifier_OUT027 = 1
        elif Outlet_Identifier == "OUT035":
            Outlet_Identifier_OUT035 = 1
        elif Outlet_Identifier == "OUT045":
            Outlet_Identifier_OUT045 = 1
        elif Outlet_Identifier == "OUT046":
            Outlet_Identifier_OUT046 = 1
        else :
            Outlet_Identifier_OUT049 = 1


        features = [Item_MRP_a,
                Item_MRP_b,
                Item_MRP_c,
                Item_MRP_d,
            Outlet_Type_Grocery_Store,
            Outlet_Type_Supermarket_Type1,
            Outlet_Type_Supermarket_Type2,
            Outlet_Type_Supermarket_Type3,
            Outlet_Size_High,
            Outlet_Size_Medium,
            Outlet_Size_Small,
            Outlet_Location_Type_Tier1,
            Outlet_Location_Type_Tier2,
            Outlet_Location_Type_Tier3,
            Outlet_Establishment_Year_1985,
            Outlet_Establishment_Year_1987,
            Outlet_Establishment_Year_1997,
            Outlet_Establishment_Year_1998,
            Outlet_Establishment_Year_1999,
            Outlet_Establishment_Year_2002,
            Outlet_Establishment_Year_2004,
            Outlet_Establishment_Year_2007,
            Outlet_Establishment_Year_2009,
            Outlet_Identifier_OUT010,
            Outlet_Identifier_OUT013,
            Outlet_Identifier_OUT017,
            Outlet_Identifier_OUT018,
            Outlet_Identifier_OUT019,
            Outlet_Identifier_OUT027,
            Outlet_Identifier_OUT035,
            Outlet_Identifier_OUT045,
            Outlet_Identifier_OUT046,
            Outlet_Identifier_OUT049]

        if 'reset' in data:
            response = ''
        else:
            result = model.predict([features])
            if(Item_MRP):
                create_pdf(Item_Type,Item_MRP,Outlet_Type,Outlet_Size,Outlet_Location_Type,Outlet_Establishment_year
                   ,Outlet_Identifier,result[0])
            response = result[0]
    
        return render_template("predict.html", response = response, data = data)
    else:
        response = ''
        return render_template("predict.html", response = response)

if __name__ == '__main__':
    app.run(debug = False)