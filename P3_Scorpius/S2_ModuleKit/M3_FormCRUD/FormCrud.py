from Packages.PackageHub import *

class FormCrud():

    def __init__(self):

        self.RenderTemplate = RenderTemplate()
        self.SelectQuery = SelectQuery()
        self.InsertQuery = InsertQuery()
        self.UpdateQuery = UpdateQuery()
        self.DeleteQuery = DeleteQuery()
        self.Exceptions = Exceptions()
        self.Response = Response()
        self.Messages = Messages()
        self.GetDate = GetDate()


    def add(self, insertQueryList, messageCode1, messageCode2, urlForText, **kwargs):

        # region Try

        try:

            # region Insert Word

            status = self.InsertQuery.generalInsert(insertQueryList)

            # endregion

            # region status 200

            if status == 200:
                return self.Response.main(messageCode=messageCode1, urlFor=urlForText)

            # endregion

            # region status 400
            
            else:
                return self.Response.main(messageCode=messageCode2, urlFor=urlForText)

            # endregion

        # endregion

        # region Exception

        except Exception as e:

            traceback.print_exc()

            return redirect(url_for("dashboard.needAuth"))

        # endregion
    
    def update(self, id, tableName, messageCode1, messageCode2, urlForText, updateColumns, **kwargs):

        # region Try

        try:

            # region Get Data ProductOne

            dataOne = self.SelectQuery.getTableFirstDataAnyFilter(tableName,{"Id" : id, "SilinmeDurumu" : 0})

            # endregion

            # region Update ProductOne 

            status = self.UpdateQuery.generalUpdate(dataOne, **updateColumns)

            # endregion

            # region status 200

            if status == 200:

                return self.Response.main(messageCode=messageCode1, urlFor=urlForText)

            # endregion

            # region status 400
            
            else:
                return self.Response.main(messageCode=messageCode2, urlFor=urlForText)

            # endregion

        # endregion

        # region Exception

        except Exception as e:

            traceback.print_exc()

            return redirect(url_for("dashboard.needAuth"))

        # endregion
    
    def delete(self, tableList, messageCode1, messageCode2, messageCode3, urlForText, **kwargs):

        # region Try

        try:

            # region Get Kwargs

            id = int(kwargs["id"])

            # endregion

            for tableName in tableList:

                # region Get DataOne

                dataOne= self.SelectQuery.getTableFirstDataAnyFilter(tableName,{"Id" : id, "SilinmeDurumu" : 0})

                # endregion

                # region Delete DataOne

                status = self.DeleteQuery.deleteGeneralOne(dataOne)

                # endregion

            # region Response

            if status == 200:
                return self.Response.main(messageCode=messageCode1, urlFor=urlForText)
            else:
                return self.Response.main(messageCode=messageCode2, urlFor=urlForText)

            # endregion

        # endregion

        # region Exception

        except Exception as e:

            self.Exceptions.mainError(messageCode3, urlFor=urlForText)
        
        # endregion