# python-gha-skeleton

Простой скелет для демонстрации GitHub Actions в Python-проектах.

Как использовать:

1. Инициализируйте репозиторий локально:
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin git@github.com:<your-username>/python-gha-skeleton.git
   git push -u origin main

2. Настройте Secrets в GitHub (Repository → Settings → Secrets and variables → Actions):
   - TEST_PYPI_API_TOKEN — токен TestPyPI (если публикуете)
   - DOCKERHUB_USERNAME, DOCKERHUB_TOKEN, DOCKERHUB_REPOSITORY — для Docker
   - (другие секреты по необходимости)

3. Примеры:
   - CI запускается на push и pull_request
   - Линтинг запускается для Python-файлов
   - Матричный тест проверяет несколько версий Python/OS
   - Публикация запускается по тегам вида vX.Y.Z

4. Перед записью урока:
   - Уберите намеренно падающий тест или используйте его как демонстрацию отладки.
   - Прогоните workflows локально (если нужно) или в тестовой ветке.
