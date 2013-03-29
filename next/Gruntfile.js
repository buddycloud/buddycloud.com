module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    connect: {
      uses_defaults: {}
    },

    regarde: {
      scripts: {
        files: '*.js',
        tasks: ['livereload']
      },

      css: {
        files: '*.css',
        tasks: ['livereload']
      }
    }
  });

  // Plug-ins
  grunt.loadNpmTasks('grunt-regarde');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-livereload');

  // Tasks
  grunt.registerTask('default', ['server']);
  grunt.registerTask('server', ['livereload-start', 'connect', 'regarde']);
}