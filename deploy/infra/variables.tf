# Use the pair values from this URL to tweak CPU/Memory values per environment:
# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-cpu-memory-error.html
variable "cpu_reservation" {
  description = "CPU reservation for an ECS task"
  default     = 256
}

variable "memory_reservation" {
  description = "Memory reservation for an ECS task"
  default     = 512
}

variable "min_task_count" {
  description = "Minimum number of ECS Tasks to have. Also used as the desired count"
  default     = 1
}

variable "max_task_count" {
  description = "Maximum number of ECS Tasks that can be scaled up to"
  default     = 3
}

variable "auto_scaling_up_threshold" {
  description = "CPU-based percentage value for triggering auto-scaling up"
  default     = 75
}

variable "auto_scaling_down_threshold" {
  description = "CPU-based percentage value for triggering auto-scaling down"
  default     = 25
}

variable "product_name" {
  default = "Market Data"
}

variable "product_version" {
  default = "1"
}

variable "default_tags" {
  type        = map(string)
  description = "Default tags for all resources"
  default     = {
    Application = "phonebook-service API"
    Service     = "phonebook-service"
    Owner       = "marketdata"
  }
}