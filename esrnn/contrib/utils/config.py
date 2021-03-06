class ModelConfig(object):
  def __init__(self, max_epochs, batch_size, batch_size_test,
               learning_rate, lr_scheduler_step_size, lr_decay, data_augmentation,
               per_series_lr_multip, gradient_eps, gradient_clipping_threshold,
               rnn_weight_decay, noise_std,
               level_variability_penalty, training_percentile, cell_type,
               state_hsize, dilations, add_nl_layer, seasonality, input_size, output_size, 
               frequency, max_periods, random_seed, device, root_dir):

    # Train Parameters
    self.max_epochs = max_epochs
    self.batch_size = batch_size
    self.batch_size_test = batch_size_test
    self.learning_rate = learning_rate
    self.lr_scheduler_step_size = lr_scheduler_step_size
    self.lr_decay = lr_decay
    self.data_augmentation = data_augmentation
    self.per_series_lr_multip = per_series_lr_multip
    self.gradient_eps = gradient_eps
    self.gradient_clipping_threshold = gradient_clipping_threshold
    self.rnn_weight_decay = rnn_weight_decay
    self.noise_std = noise_std
    self.level_variability_penalty = level_variability_penalty
    self.training_percentile = training_percentile
    self.device = device

    # Model Parameters
    self.cell_type = cell_type
    self.state_hsize = state_hsize
    self.dilations = dilations
    self.add_nl_layer = add_nl_layer
    self.random_seed = random_seed

    # Data Parameters
    self.seasonality = seasonality
    if len(seasonality)>0:
      self.naive_seasonality = seasonality[0]
    else:
      self.naive_seasonality = 1
    self.input_size = input_size
    self.input_size_i = self.input_size
    self.output_size = output_size
    self.output_size_i = self.output_size
    self.frequency = frequency
    self.min_series_length = self.input_size_i + self.output_size_i
    self.max_series_length = (max_periods * self.input_size) + self.min_series_length
    self.max_periods = max_periods
    self.root_dir = root_dir