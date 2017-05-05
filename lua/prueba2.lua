local cjson = require ("cjson");
local PreparedStatement = require ("Sql").PreparedStatement;

local cedegjson = [[{
    "number": 1092,
    "holder": "jose luis",
    "records": [{"code": "023", "name": "cuentas por pagar"},{"code": "024", "name": "cuentas por cobrar"}]
}]];

local cedeg = cjson.decode (cedegjson);

local Q = PreparedStatement:New([[SELECT "Name" FROM "AccountingAccount" WHERE "Code"='?';]]);

Q:SetString (cedeg.number);

print (Q:ToString());
