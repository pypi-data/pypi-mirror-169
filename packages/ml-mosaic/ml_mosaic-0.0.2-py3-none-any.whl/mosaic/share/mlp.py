import torch

class mlp_funnel(torch.nn.Module):
	def __init__(self, input_size, output_size, depth):
		super(mlp_funnel, self).__init__()
		self.depth = int(depth)
		self.input_size = int(input_size)
		self.output_size = int(output_size)
		self.layers = torch.nn.ModuleList()
		self.activation = torch.nn.Sigmoid()

		for i in range(self.depth):
			if i < self.depth - 1:
				self.layers.append(torch.nn.Linear(self.input_size // (2 ** i), self.input_size // (2 ** (i + 1))))
			else:
				self.layers.append(torch.nn.Linear(self.input_size // (2 ** i), self.output_size))
	
	def forward(self, data, run_info, module_info):
		for layer in self.layers:
			data = self.activation(layer(data))
		return data

	def infos(self):
		return {}

	def save_model(self, path):
		path += '.pt'
		torch.save(self, path)
	
	def load_model(self, path):
		path += '.pt'
		self = torch.load(path)


class mlp_brick(torch.nn.Module):
	def __init__(self, input_size, output_size, depth):
		super(mlp_brick, self).__init__()
		self.depth = int(depth)
		self.input_size = int(input_size)
		self.output_size = int(output_size)
		self.layers = torch.nn.ModuleList()
		self.activation = torch.nn.Sigmoid()

		for i in range(self.depth):
			if i < self.depth - 1:
				self.layers.append(torch.nn.Linear(self.input_size, self.input_size))
			else:
				self.layers.append(torch.nn.Linear(self.input_size, self.output_size))
	
	def forward(self, data, run_info, module_info):
		for layer in self.layers:
			data = self.activation(layer(data))
		return data

	def infos(self):
		return {}

	def save_model(self, path):
		path += '.pt'
		torch.save(self, path)
	
	def load_model(self, path):
		path += '.pt'
		self = torch.load(path)