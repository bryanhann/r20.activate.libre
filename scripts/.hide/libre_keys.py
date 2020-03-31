GRID="""
                              ID |                               ID | ID
                            Time |                             Time | Time
                     Record Type |                      Record Type | Type
       Historic Glucose (mmol/L) |        Historic Glucose (mmol/L) | HistBg
           Scan Glucose (mmol/L) |            Scan Glucose (mmol/L) | ScanBg
Non-numeric Rapid-Acting Insulin | Non-numeric Rapid-Acting Insulin | Rapid?
    Rapid-Acting Insulin (units) |     Rapid-Acting Insulin (units) | Rapid
                Non-numeric Food |                 Non-numeric Food | Food?
           Carbohydrates (grams) |            Carbohydrates (grams) | Carbs
 Non-numeric Long-Acting Insulin |  Non-numeric Long-Acting Insulin | Long?
     Long-Acting Insulin (units) |      Long-Acting Insulin (units) | Long
                           Notes |                            Notes | Notes
          Strip Glucose (mmol/L) |           Strip Glucose (mmol/L) | StripBg
                 Ketone (mmol/L) |                  Ketone (mmol/L) | Ketone
                             N/A |             Meal Insulin (units) | MealInsulin
                             N/A |       Correction Insulin (units) | CorrectionInsulin
                             N/A |      User Change Insulin (units) | UserChangeInsulin
                   Previous Time |                    Previous Time | PrevTime
                    Updated Time |                     Updated Time | UpdatedTime
"""
import string
ITEMS = []
for line in GRID.split('\n'):
    if '|' in line:
        ITEMS.append(map(string.strip, line.split('|')))
HONGKONG = [item[0] for item in ITEMS]
CANADA = [item[1] for item in ITEMS]
SHORT = [item[2] for item in ITEMS]
del item
del string
del line
del ITEMS
del GRID
