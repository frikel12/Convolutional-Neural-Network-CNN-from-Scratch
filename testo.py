import numpy as np
a=np.random.rand(5,5,3)
b=np.random.randint(1,3,(5,5,3))
def tensor_dot_product(tensor1, tensor2):
        if tensor1.shape != tensor2.shape:
            raise ValueError("The two tensors must have the same shape.")
        result = np.zeros(tensor1.shape)
        for k in range(tensor1.shape[0]):
            result[k] = np.dot(tensor1[k],tensor2[k].T)
        return result
print("________________________________________________________________")
print(tensor_dot_product(a,b))