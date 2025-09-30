import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# 绘制 矮病 到 锈病 的oracel性能对比图

# 示例数据
data = {
    'Encoder': ['ResNet101', 'ResNet101', 'ResNet101', 'MiT-B5',    'MiT-B5',    'MiT-B5',    'ASSFormer', 'ASSFormer', 'ASSFormer'],
    'Decoder': ['Deeplabv3', 'Segformer', 'ASSFormer', 'Deeplabv3', 'Segformer', 'ASSFormer', 'Deeplabv3', 'Segformer', 'ASSFormer'],
    'UDA (mIoU)': [80.01,     80.62,      78.52,        85.20,        83.21,        85.27,        86.03,       86.64,      86.72]
}
df = pd.DataFrame(data)

# 转换数据为适合热力图的格式
heatmap_data = pd.pivot_table(df, values='UDA (mIoU)', index='Encoder', columns='Decoder')

# 设置中文字体和英文字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 设置中文字体为宋体
plt.rcParams['font.family'] = ['Times New Roman']  # 设置英文字体为Times New Roman

# 绘制热力图
plt.figure(figsize=(10, 8))  # 设置图形的大小
sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='Reds', linewidths=.5, 
            annot_kws={"ha": "center", "va": "center", "fontsize": 16, "fontweight": "bold"})

# 设置轴标题字体
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# # 设置图例
# cbar = plt.colorbar()
# cbar.set_label('mIoU', fontsize=15)

# 显示图形
plt.title('Wheat yellow dwarf to Wheat rust (mIoU)', fontsize=25)
plt.xlabel('Decoder', fontsize=20)
plt.ylabel('Encoder', fontsize=20)
plt.savefig('oracel-y2r.png')
