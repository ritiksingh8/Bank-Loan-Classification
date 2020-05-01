from rest_framework import serializers
from . models import approvals

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=approvals
		fields='__all__'

# {
#     "Dependents":3, 
#     "ApplicantIncome":4500, 
#     "CoapplicantIncome":1500, 
#     "LoanAmount":1285000,
#     "Loan_Amount_Term":360, 
#     "Credit_History":1, 
#     "Gender_Female":0, 
#     "Gender_Male":1,
#     "Married_No":0, 
#     "Married_Yes":1, 
#     "Education_Graduate":0,
#     "Education_Not Graduate":1, 
#     "Self_Employed_No":1, 
#     "Self_Employed_Yes":0,
#     "Property_Area_Rural":1, 
#     "Property_Area_Semiurban":0,
#     "Property_Area_Urban":0
# }