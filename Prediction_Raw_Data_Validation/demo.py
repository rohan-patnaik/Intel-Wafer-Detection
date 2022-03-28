
def someFunc():
    x = 2
    print(x,x**2)

someFunc()

def manualRegexCreation():
    """
                            Method Name: manualRegexCreation
                            Description: This method contains a manually defined regex based on the "FileName" given in "Schema" file.
                                        This Regex is used to validate the filename of the training data.
                            Output: Regex pattern
                            On Failure: None

                                    """
    regex = "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
    print(regex)

manualRegexCreation()