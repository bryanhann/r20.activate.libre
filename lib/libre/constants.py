def unzip( pairs ):
    pairs = list(pairs)
    car_items = [ x for (x,y) in pairs ]
    cdr_items = [ y for (x,y) in pairs ]
    return car_items, cdr_items

IGNORE_KEYS = ['Time', 'ID', 'Type', 'N/A']

HONG_KONG_KEYLIST = unzip([
      ('ID'                              , 'ID' )
    , ('Time'                            , 'Time' )
    , ('Record Type'                     , 'Type' )
    , ('Historic Glucose (mmol/L)'       , 'HistBG' )
    , ('Scan Glucose (mmol/L)'           , 'ScanBG' )
    , ('Non-numeric Rapid-Acting Insulin', 'nnRapid' )
    , ('Rapid-Acting Insulin (units)'    , 'Rapid' )
    , ('Non-numeric Food'                , 'nnFood' )
    , ('Carbohydrates (grams)'           , 'Carbs' )
    , ('Non-numeric Long-Acting Insulin' , 'nnLong' )
    , ('Long-Acting Insulin (units)'     , 'Long' )
    , ('Notes'                           , 'Notes' )
    , ('Strip Glucose (mmol/L)'          , 'StripBG' )
    , ('Ketone (mmol/L)'                 , 'Ketone' )
    , ('N/A'                             , 'N/A' )
    , ('N/A'                             , 'N/A' )
    , ('N/A'                             , 'N/A' )
    , ('Previous Time'                   , 'Previous_Time' )
    , ('Updated Time'                    , 'Updated_Time' )
])

CANADA_KEYLIST = unzip ([
      ('ID'                              , 'ID' )
    , ('Time'                            , 'Time' )
    , ('Record Type'                     , 'Type' )
    , ('Historic Glucose (mmol/L)'       , 'HistBG' )
    , ('Scan Glucose (mmol/L)'           , 'ScanBG' )
    , ('Non-numeric Rapid-Acting Insulin', 'NNRapid' )
    , ('Rapid-Acting Insulin (units)'    , 'Rapid' )
    , ('Non-numeric Food'                , 'NNFood' )
    , ('Carbohydrates (grams)'           , 'Carbs' )
    , ('Non-numeric Long-Acting Insulin' , 'nnLong' )
    , ('Long-Acting Insulin (units)'     , 'Long' )
    , ('Notes'                           , 'Notes' )
    , ('Strip Glucose (mmol/L)'          , 'StripBG' )
    , ('Ketone (mmol/L)'                 , 'Ketone' )
    , ('Meal Insulin (units)'            , 'MealInsulin' )
    , ('Correction Insulin (units)'      , 'CorrectionInsulin')
    , ('User Change Insulin (units)'     , 'UserChangeInsulin')
    , ('Previous Time'                   , 'DateTimeOld' )
    , ('Updated Time'                    , 'DateTimeNew' )
])

KEYLISTS = [HONG_KONG_KEYLIST, CANADA_KEYLIST]

