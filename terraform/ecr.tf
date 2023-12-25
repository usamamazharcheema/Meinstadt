# ECR repository
resource "aws_ecr_repository" "greetings_repository" {
  name = "meinstadt_repo"
  force_delete = true
  tags = {
  "project" : "meinstadt_app"
  }
}