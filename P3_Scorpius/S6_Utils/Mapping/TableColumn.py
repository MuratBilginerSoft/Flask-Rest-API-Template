# region Table Column Map Class

class TableColumnMap:

    theadNameDict = {

        "office": ["Id", "Şube Adı", "Sorumlu", "Telefon", "Durum", "Oluşturma Tarihi", "Actions"],

        "staff" : ["Id", "Ad", "Soyad", "Telefon", "E-Posta", "Durum", "Actions"],

        "customer" : ["Id", "Ad", "Soyad", "Telefon", "E-Posta", "Notes", "Actions"],

        "company" : ["Id", "Firma Adı", "Sorumlu", "Telefon", "Bakiye", "Not", "Actions"],

        "product-group" : ["Id", "Ürün Grubu Id", "Grup Adı", "Not", "Oluşturan", "Oluşturma Tarihi", "Actions"],

        "unit" : ["Id", "Birim Id", "Birim Adı", "Açıklama", "Oluşturan", "Oluşturma Tarihi", "Actions"],

        "product" : ["Id", "Barkod", "Ürün Adı", "Ürün Grubu", "Birim", "Açıklama", "Actions"],

        "product-detail" : ["Id", "Barkod", "Ürün Adı", "Ürün Alış", "Ürün Satış", "Stok Alarm Seviyesi", "Actions"],

        "purchase" : ["Id", "Fatura Id", "Ürün Adı", "Miktar", "Alış Fiyatı", "Ödeme Durumu", "Actions"],

        "stock" : ["Id", "Barkod", "Ürün Adı", "Miktar", "Güncelleme Tarihi", "Revizyon", "Actions"],

    }


    columnNameDict = {

        "office" : ["Id", "OfficeName", "OfficeManager", "OfficePhone", "OfficeStatus", "CreatedAt"],

        "staff" : ["Id", "Name", "Surname", "Phone", "Email", "Status"],

        "customer" : ["Id", "Name", "Surname", "Phone", "Email", "Notes"],

        "company" : ["Id", "CompanyName", "ManagerName", "Phone", "Balance", "Notes"],

        "product-group" : ["Id", "ProductGroupId", "GroupName", "Notes", "CreatedBy", "CreatedAt"],

        "unit" : ["Id", "UnitId", "UnitName", "Description", "CreatedBy", "CreatedAt"],

        "product" : ["Id", "BarcodeNo", "ProductName", "ProductGroup", "Unit", "Description"],

        "product-detail" : ["Id", "BarcodeNo", "ProductName", "PurchasePrice", "SalesPrice", "StockAlertQuantity"],

        "purchase" : ["Id", "BillingId", "ProductName", "Quantity", "PurchasePrice", "PaymentStatus"],

        "stock" : ["Id", "BarcodeNo", "ProductName", "Quantity", "ChangedAt", "Revision"]

    }

# endregion