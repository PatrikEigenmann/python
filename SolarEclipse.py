#!/usr/bin/python3
# ***********************************************************************************************
# SolarEclipse.py - In the dead of night, when the moon is high and the stars twinkle ominously,
# there exists a Python class of unspeakable power. Its name? SolarEclipse. A name that sends
# shivers down the spines of even the bravest coders.
#
# The SolarEclipse class is no ordinary class. It’s a harbinger of darkness, a predictor of the
# celestial events that plunge the world into shadow. It calculates the exact moment when the moon
# will dare to obscure the sun, casting an eerie twilight upon the Earth.
#
# The __init__ method is where it all begins. It takes in the latitude and longitude, the coordinates
# of your location, and prepares for the impending darkness. It sets the stage, marking the time and
# place where the sun will be swallowed by the moon.
#
# But the true terror lies within the calculate method. This method, with its relentless loops and
# chilling calculations, determines the exact moment of the next solar eclipse. It checks every hour,
# for an entire year, waiting for the moment when the sun and moon align.
#
# And when that moment comes, when the moon dares to obscure the sun, the calculate method reveals
# the time of the eclipse. A time of darkness, a time of shadows, a time when the normal rules of
# day and night are thrown into chaos.
#
# So, dear coder, as you delve into the SolarEclipse class, remember this: with great power comes
# great responsibility. Use this class wisely, for it holds the power to predict the celestial
# events that have both fascinated and terrified humanity for centuries.
# -----------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -----------------------------------------------------------------------------------------------
# Fri 2023-12-29 File created.                                                  Version: 00.01
# ***********************************************************************************************
import numpy as np
import astropy.units as u
from astropy.coordinates import solar_system_ephemeris, EarthLocation, SkyCoord
from astropy.coordinates import get_body
from astropy.time import Time

class SolarEclipse:
    """
    The SolarEclipse class is no ordinary class. It’s a harbinger of darkness, a predictor of the
    celestial events that plunge the world into shadow. It calculates the exact moment when the moon
    will dare to obscure the sun, casting an eerie twilight upon the Earth.

    The __init__ method is where it all begins. It takes in the latitude and longitude, the coordinates
    of your location, and prepares for the impending darkness. It sets the stage, marking the time and
    place where the sun will be swallowed by the moon.

    But the true terror lies within the calculate method. This method, with its relentless loops and
    chilling calculations, determines the exact moment of the next solar eclipse. It checks every hour,
    for an entire year, waiting for the moment when the sun and moon align.

    And when that moment comes, when the moon dares to obscure the sun, the calculate method reveals
    the time of the eclipse. A time of darkness, a time of shadows, a time when the normal rules of
    day and night are thrown into chaos.

    So, dear coder, as you delve into the SolarEclipse class, remember this: with great power comes
    great responsibility. Use this class wisely, for it holds the power to predict the celestial
    events that have both fascinated and terrified humanity for centuries.
    """

    def __init__(self, lat, lon, height=0):
        """
        Initialize the observation point with the given latitude, longitude, and optional height.
        This constructor sets up the observation point using the specified geographical coordinates. It
        initializes the `SolarEclipse` object with the provided latitude, longitude, and height.
        Additionally, it sets the time step for hourly checks and defines the duration to check over the
        next year, ensuring the observation point is prepared for continuous monitoring and data collection.

        Args:
        lat (float): The latitude of the observation point in degrees.
        lon (float): The longitude of the observation point in degrees.
        height (float, optional): The height above the Earth's surface in meters. Default is 0.
        """
        self.location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=height*u.m)
        self.time_step = 3600  # Check every hour
        self.num_days = 365  # Check for the next year

    def calculate(self):
        """
        Calculate the times of solar eclipses observable from the specified location.
        This method uses the current time as a starting point and calculates potential solar eclipse
        occurrences over a specified number of days. It iterates through each time step, checking the
        angular separation between the sun and the moon to identify when they align closely enough to
        indicate a solar eclipse.
        
        The method makes use of the solar system ephemeris to obtain precise positions of the sun and
        moon relative to the observation point. If the angular separation is less than 0.6 degrees,
        indicating the onset of a partial eclipse, the time is recorded. The results are then printed,
        showing the time of the next solar eclipse if one is found within the given time range.
        """
        start_time = Time.now()
        end_time = start_time + self.num_days * u.day
        eclipse_times = []

        with solar_system_ephemeris.set('jpl'):
            for t in np.arange(start_time.unix, end_time.unix, self.time_step):
                time = Time(t, format='unix')
                moon = get_body('moon', time, self.location)
                sun = get_body('sun', time, self.location)
                sun_coord = SkyCoord(sun.ra, sun.dec, sun.distance, frame='icrs')
                moon_coord = SkyCoord(moon.ra, moon.dec, moon.distance, frame='icrs')

                # Check if the angular separation between the moon and sun is close to zero
                angular_separation = moon_coord.separation(sun_coord)
                if angular_separation < 0.6 * u.deg:  # Elongation where the partial eclipse begins
                    eclipse_times.append(time)

        # Print the times of the next solar eclipse
        if len(eclipse_times) > 0:
            print("The next solar eclipse is at: ", eclipse_times[0].iso)
        else:
            print("No solar eclipses found in the specified time range.")

# Example usage:
eclipse = SolarEclipse(37.7749, -122.4194)  # Coordinates for San Francisco, CA
eclipse.calculate()