def preprocess_Airline(Airline) :
    if Airline == 'Air Asia' : 
        return [0]
    elif Airline == 'Air India' :
        return [1]
    elif Airline == 'GoAir' :
        return [2]
    elif Airline == 'IndiGo' :
        return [3]
    elif Airline == 'Jet Airways' :
        return [4]
    elif Airline == 'Jet Airways Business' :
        return [5]
    elif Airline == 'Multiple carriers' :
        return [6]
    elif Airline == 'Multiple carriers Premium economy' :
        return [7]
    elif Airline == 'SpiceJet' :
        return [8]
    elif Airline == 'Trujet' :
        return [9]
    elif Airline == 'Vistara' :
        return [10]
    elif Airline == 'Vistara Premium economy' :
        return [11]
    else :
        return ["Please enter suitable Airline option"]
    
def get_Total_Stops(Total_Stops) :
    if Total_Stops.lower() == ""'non-stops' : 
        return [0]
    elif Total_Stops.lower() == '1 stops' :
        return [1]
    elif Total_Stops.lower() == '2 stops' :
        return [2]
    elif Total_Stops.lower() == '3 stops' :
        return [3]
    elif Total_Stops.lower() == '4 stops' :
        return [4]
    else :
        return ['Enter suitable Total_Stops value']

def get_Destination(Destination) :
    if Destination == 'Banglore' : 
        return [0]
    elif Destination == 'Cochin' :
        return [1]
    elif Destination == 'Delhi' :
        return [2]
    elif Destination == 'Hyderabad' :
        return [3]
    elif Destination == 'Kolkata' :
        return [4]
    else :
        return ['Enter suitable Destination Option']
    
def get_Source(Source) :
    if Source == 'Banglore' : 
        return [0]
    elif Source == 'Chennai' :
        return [1]
    elif Source == 'Delhi' :
        return [2]
    elif Source == 'Kolkata' :
        return [3]
    elif Source == 'Mumbai' :
        return [4]
    else :
        return ['Enter suitable Source Option']
    
def get_Additional_Info(Additional_Info) :
    if Additional_Info == '1 Long layover' : 
        return [0]
    elif Additional_Info == '1 Short layover' :
        return [1]
    elif Additional_Info == '2 Long layover' :
        return [2]
    elif Additional_Info == 'Business class' :
        return [3]
    elif Additional_Info == 'Change airports' :
        return [4]
    elif Additional_Info == 'In-flight meal not included' :
        return [5]
    elif Additional_Info == 'No check-in baggage included' :
        return [6]
    elif Additional_Info == 'No info' :
        return [7]
    elif Additional_Info == 'Red-eye flight' :
        return [8]
    else :
        return ['Please enter suitable Additional_Info option']
    
def get_data (data):
    
    Airline = preprocess_Airline(data['Airline'])

    Total_Stops =get_Total_Stops(data['Total_Stops'])

    Destination = get_Destination(data['Destination'])

    Source= get_Source(data['Source'])

    Additional_Info =  get_Additional_Info(data['Additional_Info'])

    final_data = Airline+Source+Destination+Total_Stops+Additional_Info
    
    #final_data =  [Day_of_Journey, Month_of_Journey, Dep_hr,Dep_min,Arrival_hr,Arrival_min,duration_hr,duration_min]+ Airline +Source+Destination+Total_Stops+Additional_Info

    return final_data


