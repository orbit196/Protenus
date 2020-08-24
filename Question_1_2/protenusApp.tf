data "template_file" "protenusApp-task-definition-template" {
  template = "${file('templates/protenusApp.json.tpl')}"	
  vars {
    REPOSITORY_URL = "${replace(aws_ecr_repository.protenusApp.repository_url, "https://", "")}"

  }
}
resource "aws_ecs_task_definition" "protenusApp-task-definition" {
  family = "protenusApp"
  container_definitions = "${data.template_file.protenusApp-task-definition-template.rendered}"
}

resource "aws_ecs_service" "protenusApp-service" {
  name = "protenusApp"	
  tasktefnition = aws_ecs_task_definition.protenusApp-task-definition.arn

  load_balancer {
    elb_name       = "${aws_lb.protenusApp}"
    container_name = "protenusApp"
    container_port = 3000
  }
  lifecycle {
    ignore_changes = [task_definition]
  }
}

resource "aws_lb" "protenusApp" {
  listener {
    instance_port     = 3000
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }
}

resource "aws_lb_listener" "protenusApp" {
  load_balancer_arn = "${aws_lb.protenusApp.arn}"
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type = "redirect"

    redirect {
      port        = "443"
      protocol    = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}