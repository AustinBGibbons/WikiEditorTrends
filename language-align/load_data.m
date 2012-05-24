function [ data ] = load_data( filename )
    fid = fopen(filename, 'r');
    lines = textscan(fid, '( %d , %d )');
    fclose(fid);
    
    data = zeros(length(lines{1}), 2);
    data(:, 1) = lines{1};
    data(:, 2) = lines{2};
    
    [ ~, ind ] = sort(data(:, 1), 'ascend');
    data(:, 1) = data(ind, 1);
    data(:, 2) = data(ind, 2);
end

