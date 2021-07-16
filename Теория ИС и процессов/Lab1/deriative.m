function f = deriative(x)
b = zeros(1, length(x));
for i = 2:length(x)
    b(i) = x(i-1)*(length(x)-i+1);
end
f = b;