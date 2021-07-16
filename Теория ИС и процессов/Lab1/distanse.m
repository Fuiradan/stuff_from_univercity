function f  = distanse(a, x, x0, y0)

f = sqrt((x - x0).^2+(polyval(a, x) - y0).^2);
end

