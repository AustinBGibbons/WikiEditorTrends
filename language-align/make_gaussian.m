function [ shape ] = make_gaussian( width )
    if width == 1
       shape = [ 1 ];
       return;
    end

    shape = zeros(1, width);
    for i = 1 : width
       z = (i - 0.5) / width - 0.5;
       shape(i) = normpdf(z*5);
    end
end

