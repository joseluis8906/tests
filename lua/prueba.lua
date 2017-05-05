function GenerateSessionId (PseudoId)
    local Dict = "0X1P2QV4cCUdeAfgMhijEklmnS5OpZ@qrKsWt9vIw7by6zBu-DF3H.x8JaL_NRoTYG";
    local DictLen = string.len (Dict);
    local Index = 0;
    local Pch = 0;
    local SessionId = "";
    local Salt = os.time();
    PseudoId = string.sub(tostring(Salt-64), -3, -1)..PseudoId..string.sub(tostring(Salt+64), -3, -1);
    local Len = string.len (PseudoId);
    print (PseudoId);

    for i=1, Len do
        Index = string.find (Dict, string.sub (PseudoId, i, i));
        Index = Index + 13;
        
        if Index > DictLen then
            Index = Index - DictLen;
        end
        
        SessionId = SessionId..string.sub(Dict, Index, Index);
    end

    print (SessionId)
end


local username = "root";
local password = "1234";
local Q = ("SELECT \"UserName\" FROM \"AuthUser\" WHERE \"UserName\"='%s' AND \"Password\"='%s';"):format (username, password);

local res = {
    {UserName = "Jose", Password = "1234"},
};

for i, o in ipairs (res) do
    for k, v in pairs (o) do
        print (v);
    end
end