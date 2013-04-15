module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    connect: {
      uses_defaults: {}
    },

    regarde: {
      staticfiles: {
        files: 'scripts/*.js, *.css, *.html',
        tasks: ['livereload', 'cssmin', 'uglify']
      },

      css: {
        files: 'css/**/*.css',
        tasks: ['cssmin']
      },

      js: {
        files: 'js/**/*.js',
        tasks: ['uglify']
      }
    },

    cssmin: {
      compress: {
        files: {
          'style.min.css': ['css/**/*.css']
        }
      }
    },

    uglify: {
      my_target: {
        files: {
          'scripts.min.js': ['js/vendor/prettify.js', 'js/vendor/jquery.waypoints.js', 'js/scripts.js']
        }
      }
    }
  });

  // Plug-ins
  grunt.loadNpmTasks('grunt-regarde');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-livereload');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Tasks
  grunt.registerTask('default', ['server']);
  grunt.registerTask('server', ['livereload-start', 'connect', 'cssmin', 'uglify', 'regarde']);
}