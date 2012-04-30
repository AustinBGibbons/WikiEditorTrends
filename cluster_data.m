%% prepare normalized data
userData = dataset(:, 2:end); % remove id col
validSubset = userData(userData(:, 1) > 0);
userData = userData(validSubset, :); % clear users with no revs
userData = [ userData(:, 2:end) ./ repmat(userData(:, 1), 1, 5) ]; % normalize others by numEdits
userData = userData - repmat(mean(userData, 1), size(userData, 1), 1);
userData = userData ./ repmat(std(userData, 1), size(userData, 1), 1);

%% k-means clustering
[ means, C ] = kmeans(userData, 5, 'emptyaction', 'singleton');
hist(means);

%% t-sne and plot a subset
addpath tSNE/
subset = randperm(size(userData, 1));
numPoints = 100;
ydata = tsne(userData(subset(1:numPoints), :), [], 2, 5);
colors = cell(1);
colors{1} = 'b';
colors{2} = 'm';
colors{3} = 'g';
colors{4} = 'r';
colors{5} = 'c';
colors{6} = 'k';
colors{7} = 'y';

figure(1);
clf;
axis([ min(ydata(:, 1)) max(ydata(:, 1)) min(ydata(:, 2)) max(ydata(:, 2)) ]);
hold on;
for i = 1 : numPoints
    text(ydata(i, 1), ydata(i, 2), num2str(means(subset(i))), 'color', colors{mod(means(subset(i))-1, 7)+1});
end
hold off;