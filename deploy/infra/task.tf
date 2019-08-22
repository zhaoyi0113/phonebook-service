# See here for details: https://github.com/oneiress/tf-module-marketdata-service
module "api" {
  source                      = "git@github.com:oneiress/tf-module-marketdata-service"

  name                        = "${module.ci.app_name}-api"
  service_type                = "api"
  deploy_env                  = module.ci.deploy_env
  lob                         = "marketdata"  
  min_task_count              = var.min_task_count
  max_task_count              = var.max_task_count
  auto_scaling_up_threshold   = var.auto_scaling_up_threshold
  auto_scaling_down_threshold = var.auto_scaling_down_threshold

  container_definitions       = data.template_file.container_def.rendered
  cpu_reservation             = var.cpu_reservation
  memory_reservation          = var.memory_reservation
  alb_healthcheck_path        = "/v2/openapi.json"  
  has_task_policy             = "false"

  repository_base_url         = module.ci.repository_base_url
  product_name                = var.product_name
  product_version             = var.product_version
  app_version                 = module.ci.app_version
  tags                        = merge(module.ci.remote_state.tags.default, var.default_tags)
}

data "template_file" "container_def" {
  template          = "${file("${path.module}/src/container-def.json")}"
  vars = {
    IMAGE_URL       = "${module.ci.repository_base_url}/marketdata/${module.ci.app_name}:${module.ci.app_version}"
    REGION          = module.ci.region
    DEPLOY_ENV      = module.ci.deploy_env
    APP_NAME        = "${module.ci.app_name}-api"
    APP_VERSION     = module.ci.app_version
    PRODUCT_NAME    = var.product_name
    PRODUCT_VERSION = var.product_version
    LOG_GROUP_NAME  = module.ci.remote_state.apps.log_group_name
  }
}