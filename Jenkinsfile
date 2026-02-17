pipeline {
    agent any

    stages {
        // СТАДИЯ 1: Кодты алу
        stage('Checkout Code') {
            steps {
                echo 'Забираем код из GitHub...'
                checkout scm
            }
        }
        
        // СТАДИЯ 2: Файлдарды тексеру
        stage('Check Files') {
            steps {
                echo ' 📄  Проверяем созданные файлы...'
                sh '''
                    echo "=== ФАЙЛЫ В РЕПОЗИТОРИИ ==="
                    ls -la
                    echo ""
                    echo "=== ПРОВЕРКА НАШИХ ФАЙЛОВ ==="
                    if [ -f Dockerfile ]; then
                        echo "Dockerfile найден"
                        head -10 Dockerfile
                    else
                        echo "Dockerfile не найден"
                    fi
                    
                    if [ -f requirements.txt ]; then
                        echo "requirements.txt найден"
                    else
                        echo "requirements.txt не найден"
                    fi
                    
                    if [ -d src ]; then
                        echo "Папка src найдена"
                        if [ -f src/app.py ]; then
                            echo "Файл src/app.py найден"
                        else
                            echo "Файл src/app.py не найден"
                        fi
                    else
                        echo "Папка src не найдена"
                    fi
                '''
            }
        }
        
        // СТАДИЯ 3: Docker теориясы
        stage('Docker Theory') {
            steps {
                echo 'ТЕОРИЯ DOCKER'
                echo 'Если бы Jenkins не был в Docker, мы бы выполнили:'
                echo '1. docker build -t my-app .'
                echo '2. docker run -d -p 8081:5000 my-app'
                echo '3. curl http://localhost:8081/health'
                echo ''
                echo 'Но так как Jenkins в Docker, эти команды могут не работать.'
            }
        }
        
        // СТАДИЯ 4: Docker командаларын тексеру
        stage('Try Docker Commands') {
            steps {
                echo ' 🔧  Пробуем Docker команды...'
                script {
                    try {
                        sh 'docker --version || echo "Docker не доступен"'
                        sh '''
                            echo "Пробуем собрать Docker образ..."
                            docker build -t test-image . 2>/dev/null || echo "Не удалось собрать образ"
                        '''
                    } catch (Exception e) {
                        echo "Docker команды не работают. Это ожидаемо!"
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo ' === ИТОГ РАБОТЫ ==='
            sh '''
                echo "Дата: $(date)"
                echo "1. Код -> GitHub"
                echo "2. GitHub -> Jenkins"
                echo "3. Jenkins проверяет файлы"
                echo "4. Docker теория изучена"
            '''
        }
        success {
            echo 'ОТЛИЧНО! Вы поняли процесс CI/CD!'
        }
        failure {
            echo 'Были ошибки, но это часть обучения!'
        }
    }
}
