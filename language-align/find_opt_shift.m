function [ shift, tscore ] = find_opt_shift( lang_data, ordering )
    len = size(lang_data, 1);
    shift = zeros(1, len);
    tscores = zeros(1, len);
    
    for i = 2 : len        
        base = ordering(i-1);
        curve = ordering(i);
        
        shift_range = max(max(lang_data{base, 1}), max(lang_data{curve, 1})) -...
                      min(min(lang_data{base, 1}), min(lang_data{curve, 1}));
                  
        shift_range = floor(shift_range / 8);
                  
        base_data = lang_data{base, 2};
        curve_data = lang_data{curve, 2};
        sd = length(base_data) - length(curve_data);
        if sd > 0
           base_data = base_data((sd+1):end);
        elseif sd < 0
           curve_data = curve_data((1-sd):end); 
        end
        
        base_data = base_data / max(base_data);
        curve_data = curve_data / max(curve_data);
        
        best_shift = 0;
        best_score = -inf;
        for j = -shift_range : shift_range
            if j < 0
                data1 = base_data(1:end+j);
                data2 = curve_data(1-j:end);
            elseif j > 0
                data1 = base_data(j+1:end);
                data2 = curve_data(1:end-j);
            else
                data1 = base_data;
                data2 = curve_data;
            end
            
%             figure(2);
%             clf;
%             hold on;
%             plot(data1, 'b');
%             plot(data2, 'r');
%             hold off;
            
            %score = JSDiv(data1', data2');
            score = corr(data1, data2);
            if score > best_score
               best_score = score;
               best_shift = j;
            end
        end
        
        shift(i) = best_shift;
        tscores(i) = best_score;
        
        %fprintf('Alignment %d find best score %f shift %d\n', i, best_score, best_shift);
    end
    
    tscore = 1.0 / sum(1 ./ (tscores+0.001));
end

