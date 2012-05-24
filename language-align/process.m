%%
languages = {
  'japan',...
  'arabic',...
  'bosnia',...
  'china',...
  'polish',...
  'portugal'
};

iters = 2500;
smooth_size = 5;
smoother = make_gaussian(smooth_size);

%%

% load data for languages
lang_data = cell(1, 2);
for l = 1 : length(languages)
    lang = languages{l};
    
    
    data = load_data([lang, '.time.2011']);
    graph = conv(data(:, 2), smoother);
    
    lang_data{l, 1} = data(:, 1);
    lang_data{l, 2} = graph(smooth_size:end);
end

% find a good alignment given a starting permutation
opt_shift = [];
best_score = 0;
for iter = 1 : iters
    perm = randperm(length(languages));
    [ shift, score ] = find_opt_shift(lang_data, perm);
    fprintf('Iter %d, score %f\n', iter, score);
    if score > best_score
       best_score = score;
       opt_shift = shift;
    end
end

%%
figure(1);
clf;
hold on;
for l = 1 : length(languages)
    plot(lang_data{l, 1}, lang_data{l, 2} / sum(lang_data{l, 2}));
end
hold off;

figure(2);
clf;
hold on;
for l = 1 : length(languages)
    plot(lang_data{l, 1} + opt_shift(l), lang_data{l, 2} / sum(lang_data{l, 2}));
end
hold off;
