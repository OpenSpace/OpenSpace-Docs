// OpenSpace-Docs CI pipeline
//
// Lints the Markdown content, validates the images and builds the Sphinx documentation
// without deploying it
//
// Required plugins: Pipeline, Git, Docker, Workspace Cleanup
//
// The job runs in an Ubuntu 24.04 container with Python 3.12 and Node.js 22,
// mirroring the Read the Docs build environment (.readthedocs.yml). The agent
// needs a Linux node with Docker available.

def url = 'https://github.com/OpenSpace/OpenSpace-Docs'
def branch = env.BRANCH_NAME

// The CHANGE_BRANCH only exists if we are building a PR branch in which case it returns
// the original branch
if (env.CHANGE_BRANCH) {
  branch = env.CHANGE_BRANCH
}

// Checks out the repository. In contrast to a manual `git clone`, this reports the commit
// and the changelog back to Jenkins
def scmConfig = scmGit(
  userRemoteConfigs: [[url: url]],
  branches: [[name: "*/${branch}"]],
  extensions: [
    cleanBeforeCheckout(),
    cloneOption(shallow: true, depth: 1, noTags: true, timeout: 30)
  ]
)

pipeline {
  agent {
    docker {
      image 'ubuntu:24.04'
    }
  }

  options {
    // git is installed in the Setup stage before the repository is checked out
    skipDefaultCheckout(true)
    timeout(time: 30, unit: 'MINUTES')
  }

  stages {
    stage('Setup') {
      steps {
        sh '''
          set -e
          export DEBIAN_FRONTEND=noninteractive
          apt-get update
          apt-get install -y --no-install-recommends git ca-certificates curl python3 python3-venv python3-pip
          curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
          bash nodesource_setup.sh
          apt-get install -y --no-install-recommends nodejs
          python3 --version
          node --version
          npm --version
        '''
        checkout scmConfig
        sh '''
          set -e
          python3 -m venv .venv
          .venv/bin/pip install --upgrade pip
          # pillow is only needed by scripts/check_images.py
          .venv/bin/pip install -r requirements.txt pillow
          npm ci
        '''
      }
    }

    stage('Lint Markdown') {
      steps {
        sh 'npx markdownlint-cli -c .markdownlint.json -i build -i node_modules "**/*.md"'
      }
    }

    stage('Check Images') {
      steps {
        sh '.venv/bin/python scripts/check_images.py'
      }
    }

    stage('Build Documentation') {
      steps {
        // -W treats warnings as errors, matching the Read the Docs build
        sh '.venv/bin/sphinx-build -b html -W . build/html'
        sh 'test -f build/html/index.html'
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}
