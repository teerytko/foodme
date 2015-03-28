{spawn} = require 'child_process'

coffee = "coffee"

option '-p', '--port [PORT_NUMBER]', 'set the port number for `start`'
option '-s', '--settings [SETTINGS_NAME]', 'set the settings file for `start`'
option '-e', '--environment [ENVIRONMENT_NAME]', 'set the environment for `start`'

task 'build', 'Build the coffee files to js', (options) ->
  process.env.NODE_ENV = options.environment ? 'development'
  args = [
    '--compile',
    '--output', 'public/js'
    'uisrc',
  ]
  spawn coffee, args, stdio: 'inherit'

task 'watch', 'Start coffee --watch for the coffee files to js', (options) ->
  process.env.NODE_ENV = options.environment ? 'development'
  args = [
    '--compile',
    '--watch',
    '--output', 'public/js'
    'uisrc'
  ]
  spawn coffee, args, stdio: 'inherit'
