import numpy as np

#cretae data shape
sales = [12000, 13500, 15000, 14200, 16800, 18500]
months = ["Jan","Feb","Mar","Apr","May","Jun"]
orders = [320, 350, 380, 360, 420, 450]
customers = [280, 300, 330, 315, 360, 390]

#use dict establish indicator mapping
data_dict = {
    'sales': sales,
    'orders': orders,
    'customers': customers
}

#covert the lists to 1D numpy arrays
sales_array = np.array(sales)
customers_array = np.array(customers)
orders_array = np.array(orders)

#create the 2D numpy array
data = np.array([
    sales_array,
    orders_array,
    customers_array
])

#data processing
##sales
s_sum = sales_array.sum()
s_min = sales_array.min()
s_max = sales_array.max()
s_mean =  sales_array.mean()
##customers
c_sum = customers_array.sum()
c_min = customers_array.min()
c_max = customers_array.max()
c_mean =  customers_array.mean()
##orders
o_sum = orders_array.sum()
o_min = orders_array.min()
o_max = orders_array.max()
o_mean =  orders_array.mean()
##index
max_sales_index = np.argmax(sales_array)
min_sales_index = np.argmin(sales_array)

#print test
print("========== 经营数据 ==========")
print("月份：", months)
print("销售额：", sales)
print("订单量：", orders)
print("客户数量：", customers)

print("\n========== 经营数据字典 ==========")
print(data_dict)

print("\n========== NumPy 一维数组 ==========")
print("销售额数组：", sales_array)
print("订单量数组：", orders_array)
print("客户数量数组：", customers_array)

print("\n========== 二维经营数据数组 ==========")
print(data)

print("\n========== 数组结构信息 ==========")

print("shape =", data.shape)
print("ndim  =", data.ndim)
print("size  =", data.size)
print("dtype =", data.dtype)

print("\n========== 销售额统计 ==========")

print("销售额总和：", s_sum)
print("销售额平均值：", s_mean)
print("销售额最大值：", s_max)
print("销售额最小值：", s_min)

print("\n========== 订单量统计 ==========")

print("订单量总和：", o_sum)
print("订单量平均值：", o_mean)
print("订单量最大值：", o_max)
print("订单量最小值：", orders_array.min())

print("\n========== 客户数量统计 ==========")

print("客户数量总和：", c_sum)
print("客户数量平均值：", c_mean)
print("客户数量最大值：", c_max)
print("客户数量最小值：", c_min)

print("\n========== 销售额最高/最低月份 ==========")
print(
    "销售额最高月份：",
    months[max_sales_index],
    "，销售额：",
    sales_array[max_sales_index]
)
print(
    "销售额最低月份：",
    months[min_sales_index],
    "，销售额：",
    sales_array[min_sales_index]
)
