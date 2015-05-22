'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var uglify = require('gulp-uglify');
var gulpif = require('gulp-if');
var exec = require('child_process').exec;
 
 
var notify = require('gulp-notify');
 
var buffer = require('vinyl-buffer');
var argv = require('yargs').argv;
// sass & less
var sass = require('gulp-sass');
var less = require('gulp-less');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer-core');
var sourcemaps = require('gulp-sourcemaps');
// BrowserSync
var browserSync = require('browser-sync');
// js
var watchify = require('watchify');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
// image optimization
var imagemin = require('gulp-imagemin');
// linting
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
// testing/mocha
var mocha = require('gulp-mocha');
 
// gulp build --production
var production = !!argv.production;
// determine if we're doing a build
// and if so, bypass the livereload
var build = argv._.length ? argv._[0] === 'build' : false;
var watch = argv._.length ? argv._[0] === 'watch' : true;
 
// ----------------------------
// Error notification methods
// ----------------------------
var beep = function() {
  var os = require('os');
  var file = 'gulp/error.wav';
  if (os.platform() === 'linux') {
    // linux
    exec("aplay " + file);
  } else {
    // mac
    console.log("afplay " + file);
    exec("afplay " + file);
  }
};
var handleError = function(task) {
  return function(err) {
    beep();
    
      notify.onError({
        message: task + ' failed, check the logs..',
        sound: false
      })(err);
    
    gutil.log(gutil.colors.bgRed(task + ' error:'), gutil.colors.red(err));
  };
};
// --------------------------
// CUSTOM TASK METHODS
// --------------------------
var tasks = {
  // --------------------------
  // Delete build folder
  // --------------------------
  clean: function(cb) {
    del(['./voluntagme/static/build'], cb);
  },
  // --------------------------
  // Copy static assets
  // --------------------------
  assets: function() {
    return gulp.src('./voluntagme/static/assets/**/*')
      .pipe(gulp.dest('./voluntagme/static/build/assets/'));
  },
  // --------------------------
  // HTML
  // --------------------------
  // html templates (when using the connect server)
  templates: function() {
    // gulp.src('./voluntagme/templates/*.html')
    //   .pipe(gulp.dest('build/'));
  },
  // --------------------------
  // SASS (libsass)
  // --------------------------
  sass: function() {
    return gulp.src('./voluntagme/static/scss/style.scss')
      // sourcemaps + sass + error handling
      .pipe(gulpif(!production, sourcemaps.init()))
      .pipe(sass({
        sourceComments: !production,
        outputStyle: production ? 'compressed' : 'nested'
      }))
      .on('error', handleError('SASS'))
      // generate .maps
      .pipe(gulpif(!production, sourcemaps.write({
        'includeContent': false,
        'sourceRoot': '.'
      })))
      // autoprefixer
      .pipe(gulpif(!production, sourcemaps.init({
        'loadMaps': true
      })))
      .pipe(postcss([autoprefixer({browsers: ['last 2 versions']})]))
      // we don't serve the source files
      // so include scss content inside the sourcemaps
      .pipe(sourcemaps.write({
        'includeContent': true
      }))
      // write sourcemaps to a specific directory
      // give it a file and save
      .pipe(gulp.dest('./voluntagme/static/css'));
  },
  less: function() {
    return gulp.src('./voluntagme/static/less/*.less')
      // sourcemaps + sass + error handling
      .pipe(gulpif(!production, sourcemaps.init()))
      .pipe(less())
      .on('error', handleError('LESS'))
      // generate .maps
      .pipe(gulpif(!production, sourcemaps.write({
        'includeContent': false,
        'sourceRoot': '.'
      })))
      // autoprefixer
      .pipe(gulpif(!production, sourcemaps.init({
        'loadMaps': true
      })))
      .pipe(postcss([autoprefixer({browsers: ['last 2 versions']})]))
      // we don't serve the source files
      // so include scss content inside the sourcemaps
      .pipe(sourcemaps.write({
        'includeContent': true
      }))
      // write sourcemaps to a specific directory
      // give it a file and save
      .pipe(gulp.dest('./voluntagme/static/css/'));
  },
  // --------------------------
  // Browserify
  // --------------------------
  browserify: function() {
    var bundler = browserify('./voluntagme/static/js/app.js', {
      debug: !production,
      cache: {}
    });
    // determine if we're doing a build
    // and if so, bypass the livereload
    var build = argv._.length ? argv._[0] === 'build' : false;
    if (watch) {
      bundler = watchify(bundler);
    }
    var rebundle = function() {
      return bundler.bundle()
        .on('error', handleError('Browserify'))
        .pipe(source('./voluntagme/static/js/build.js'))
        .pipe(gulpif(production, buffer()))
        .pipe(gulpif(production, uglify()))
        .pipe(gulp.dest('./'));
    };
    bundler.on('update', rebundle);
    return rebundle();
  },
  // --------------------------
  // linting
  // --------------------------
  lintjs: function() {
    return gulp.src([
        'gulpfile.js',
        './voluntagme/static/js/index.js',
        './voluntagme/static/js/**/*.js'
      ]).pipe(jshint())
      .pipe(jshint.reporter(stylish))
      .on('error', function() {
        beep();
      });
  },
  // --------------------------
  // Optimize asset images
  // --------------------------
  optimize: function() {
    return gulp.src('./voluntagme/static/assets/**/*.{gif,jpg,png,svg}')
      .pipe(imagemin({
        progressive: true,
        svgoPlugins: [{removeViewBox: false}],
        // png optimization
        optimizationLevel: production ? 3 : 1
      }))
      .pipe(gulp.dest('./voluntagme/static/assets/'));
  },
  // --------------------------
  // Testing with mocha
  // --------------------------
  test: function() {
    return gulp.src('./client/**/*test.js', {read: false})
      .pipe(mocha({
        'ui': 'bdd',
        'reporter': 'spec'
      })
    );
  },
 
 
};
 
gulp.task('browser-sync', function() {
    browserSync({
        proxy: 'localhost:8000',
        port: process.env.PORT || 3000
    });
});
 
gulp.task('reload-sass', ['sass'], function(){
  browserSync.reload();
});
gulp.task('reload-less', ['less'], function(){
  browserSync.reload();
});
gulp.task('reload-js', ['browserify'], function(){
  browserSync.reload();
});
gulp.task('reload-templates', ['templates'], function(){
  browserSync.reload();
});
 
// --------------------------
// CUSTOMS TASKS
// --------------------------
gulp.task('clean', tasks.clean);
// for production we require the clean method on every individual task
var req = build ? ['clean'] : [];
// individual tasks
gulp.task('templates', req, tasks.templates);
gulp.task('assets', req, tasks.assets);
gulp.task('sass', req, tasks.sass);
gulp.task('less', req, tasks.less);
gulp.task('browserify', req, tasks.browserify);
gulp.task('lint:js', tasks.lintjs);
gulp.task('optimize', tasks.optimize);
gulp.task('test', tasks.test);
 
// --------------------------
// DEV/WATCH TASK
// --------------------------
gulp.task('watch', ['assets', 'templates', 'sass', 'less', 'browserify', 'browser-sync'], function() {
 
  // --------------------------
  // watch:sass
  // --------------------------
  gulp.watch('./voluntagme/static/scss/**/*.scss', ['reload-sass']);
  
  // --------------------------
  // watch:less
  // --------------------------
  gulp.watch('./voluntagme/static/less/**/*.less', ['reload-less']);
 
  // --------------------------
  // watch:js
  // --------------------------
  gulp.watch('./voluntagme/static/js/**/*.js', ['lint:js', 'reload-js']);
 
  // --------------------------
  // watch:html
  // --------------------------
  gulp.watch('./voluntagme/templates/**/*.html', ['reload-templates']);
 
  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});
 
// build task
gulp.task('build', [
  'clean',
  'templates',
  'assets',
  'sass',
  'browserify'
]);
 
gulp.task('default', ['watch']);
 
// gulp (watch) : for development and livereload
// gulp build : for a one off development build
// gulp build --production : for a minified production build