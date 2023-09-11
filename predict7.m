% 加载神经网络模型
load('net.mat');

% 输入测试数据，这里示例为4行1列的矩阵
% 替换以下示例数据为您的输入数据
input_data = [4; 110; 1500; 40];

% 进行推理
output = sim(net, input_data); 

% 四舍五入输出结果
rounded_output = round(output);

% 显示结果
disp(rounded_output);