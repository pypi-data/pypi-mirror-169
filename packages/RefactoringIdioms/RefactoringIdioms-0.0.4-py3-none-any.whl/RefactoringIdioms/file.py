def test_stop_training_csv(self):
    # Test that using the CSVLogger callback with the TerminateOnNaN callback
    # does not result in invalid CSVs.
    np.random.seed(1337)
    tmpdir = self.get_temp_dir()
    self.addCleanup(shutil.rmtree, tmpdir, ignore_errors=True)

    with self.cached_session():
        fp = os.path.join(tmpdir, 'test.csv')
        (x_train, y_train), (x_test, y_test) = testing_utils.get_test_data(
            train_samples=TRAIN_SAMPLES,
            test_samples=TEST_SAMPLES,
            input_shape=(INPUT_DIM,),
            num_classes=NUM_CLASSES)

        y_test = np_utils.to_categorical(y_test)
        y_train = np_utils.to_categorical(y_train)
        cbks = [keras.callbacks.TerminateOnNaN(), keras.callbacks.CSVLogger(fp)]
        model = keras.models.Sequential()
        for _ in range(5):
            model.add(keras.layers.Dense(2, input_dim=INPUT_DIM, activation='relu'))
        model.add(keras.layers.Dense(NUM_CLASSES, activation='linear'))
        model.compile(loss='mean_squared_error',
                      optimizer='rmsprop')

        history = model.fit_generator(data_generator(),
                                      len(x_train) // BATCH_SIZE,
                                      validation_data=(x_test, y_test),
                                      callbacks=cbks,
                                      epochs=20)
        loss = history.history['loss']
        assert len(loss) > 1
        assert loss[-1] == np.inf or np.isnan(loss[-1])
    values = []
    with open(fp) as f:
        # On Windows, due to \r\n line ends, we may end up reading empty lines
        # after each line. Skip empty lines.
        for x in csv.reader(f):
            if x:
                values.append(x)
    assert 'nan' in values[-1], 'The last epoch was not logged.'
