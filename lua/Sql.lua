PreparedStatement = {
    Stm = ""
};

function PreparedStatement:New (Stm)
    o = o or {};
    setmetatable(o, self);
    self.__index = self;
    self.Stm = Stm;
    return o
end

function PreparedStatement:SetString (V)
    self.Stm = self.Stm:gsub ("?", "'"..tostring(V).."'");
end

function PreparedStatement:ToString ()
    return self.Stm;
end

return {PreparedStatement = PreparedStatement}