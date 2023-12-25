resource "aws_lambda_function" "greetings_function" {
  function_name = "meinstadt_lambda"
  architectures = ["arm64"]
  role          = aws_iam_role.iam_for_lambda.arn
  package_type  = "Image"
  timeout       = 600
  memory_size   = 3008
  image_uri     = "${aws_ecr_repository.greetings_repository.repository_url}:latest"
}