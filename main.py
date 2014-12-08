#!/usr/bin/python

"""
Module permettant le lancement de l'application et sa configuration
"""

__author__ =  'Emile Taverne'
__version__=  '0.6'

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

import os
import sys
import ConfigParser
import math

from GameScreens.ConnexionScreen import ConnexionScreen
from GameScreens.QGScreen import QGScreen 

fichierConfig = "config.ini";

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
	
config_path = os.path.join(application_path, fichierConfig)

class Game(App):
	"""Application a la base du jeu"""
	
	Config = ConfigParser.ConfigParser()
	Config.read(config_path)
	
	title = Config.get("General", "Titre")
	icon = Config.get("General", "Icon")
		
	def build(self):
		"""Configure l'affichage selon le systeme d'exploitation courrant et initialise le widget de base"""
		
		self.Config = ConfigParser.ConfigParser()
		self.Config.read(config_path)
		
		from kivy.base import EventLoop
		EventLoop.ensure_window()
		self.window = EventLoop.window

		self.root = InterfaceManager()
		
		self.configurer()
		
	def configurer(self):
		from kivy import platform
		if platform == 'linux':
			self.linuxConfig()
		elif platform == 'android':
			self.androidConfig()
		elif platform == 'macosx':
			self.macosxConfig
		elif platform == 'ios':
			self.iosConfig()
		elif platform == 'win':
			self.winConfig()
		else:
			self.defaultConfig()		
			
		print
		print
		print platform
		print
		print
				
	def linuxConfig(self):
		"""Configuration des sytemes linux"""
		self.window.fullscreen = self.Config.get("Graphismes", "ScreenMode") == "Fullscreen"
		self.window.borderless = self.Config.get("Graphismes", "ScreenMode") == "Borderless"
		self.window.size = (int(self.Config.get("Graphismes", "Width")), int(self.Config.get("Graphismes", "Height")))
		
		self.root.keyboard = Window.request_keyboard(self.root.keyboard_closed, self.root)
		self.root.keyboard.bind(on_key_down=self.root.on_keyboard_down)
		
	def androidConfig(self):
		"""Configuration des sytemes android"""
		pass
		
	def macosxConfig(self):
		"""Configuration des sytemes osx"""
		self.window.fullscreen = self.Config.get("Graphismes", "ScreenMode") == "Fullscreen"
		self.window.borderless = self.Config.get("Graphismes", "ScreenMode") == "Borderless"
		self.window.size = (int(self.Config.get("Graphismes", "Width")), int(self.Config.get("Graphismes", "Height")))
		
		self.root.keyboard = Window.request_keyboard(self.root.keyboard_closed, self.root)
		self.root.keyboard.bind(on_key_down=self.root.on_keyboard_down)
		
	def iosConfig(self):
		"""Configuration des sytemes ios"""
		self.window.fullscreen = True
		self.window.size = self.window.system_size()
		
	def winConfig(self):
		"""Configuration des sytemes windows"""
		self.window.fullscreen = self.Config.get("Graphismes", "ScreenMode") == "Fullscreen"
		self.window.borderless = self.Config.get("Graphismes", "ScreenMode") == "Borderless"
		self.window.size = (int(self.Config.get("Graphismes", "Width")), int(self.Config.get("Graphismes", "Height")))
		
		self.root.keyboard = Window.request_keyboard(self.root.keyboard_closed, self.root)
		self.root.keyboard.bind(on_key_down=self.root.on_keyboard_down)
		
	def defaultConfig(self):
		"""Configuration des sytemes non reconnus"""
		self.window.fullscreen = True
		self.window.size = self.window.system_size()
		
class InterfaceManager(FloatLayout):
	"""Widget gerant les differents ecrans qui peuvent etre affiches"""
	app = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		"""Initialisation et affiche l'ecran de connexion"""
		super(InterfaceManager, self).__init__(**kwargs)
		
		self.configurationPopup = ConfigurationDialog(attach_to=self, app=self)
		self.menuPopup = MenuDialog(app=self)
		
		self.changeScreen("ConnexionScreen")

	def build(self):
		"""Rajoute les elements communs a tous les screens"""
		conf = Button(size_hint=(None, None), size=("50dp", "50dp"), pos=("5dp", "5dp"), on_press=self.menu)
		conf.add_widget(Image(source="Images/reglages.png", size_hint=(None, None), size=conf.size, pos=conf.pos))
		self.add_widget(conf)
		
	def changeScreen(self, screen):
		"""Methode permettant de changer l'ecran qui est affiche
		
		Arguments:
			screen -- Nom de l'ecran a afficher"""
		self.clear_widgets()
		if screen == "ConnexionScreen":
			self.add_widget(ConnexionScreen(app=self))
		elif screen == "QGScreen":
			self.add_widget(QGScreen(app=self))
		elif screen == "GameScreen":
			self.add_widget(GameScreen(app=self))
		else:
			print "GameScreen inconnu : ", screen
			self.changeScreen("ConnexionScreen")		
		self.build()
			
	def keyboard_closed(self):
		"""Methode appelee si les clavier est desactive, enleve le binding cree"""
		self.keyboard.unbind(on_key_down=self.on_keyboard_down)
		self.keyboard = None
		
	def on_keyboard_down(self, keyboard, keycode, text, modifiers):
		"""Declanche differentes actions selon les actions de l'utilisateur au clavier"""
		if keycode[1] == 'escape':
			self.menu(None)
		return True
		
	def menu(self, instance):
		"""Affiche ou cache le menu"""
		if self.configurationPopup.etat == False:
			if self.menuPopup.etat == False:
				self.menuPopup.open()
			else:
				self.menuPopup.dismiss()
		
	def configuration(self):
		"""Affiche ou cache la fenetre de configuration"""
		if self.configurationPopup.etat == False:
			self.configurationPopup.open()
		else:
			self.configurationPopup.dismiss()

	def quitter(self):
		"""Ferme l'application"""
		App.get_running_app().stop()
		
class ConfigurationDialog(Popup):
	"""Widget permettant de configurer l'application selon les preferences de l'utilisateur"""
	app = ObjectProperty(None)
	title = "Configuration"
	auto_dismiss = False
	
	def __init__(self, **kwargs):
		super(Popup, self).__init__(**kwargs)
		self.etat = False
		
		self.Config = ConfigParser.ConfigParser()
		self.Config.read(config_path)
		
		self.initialiserValeurs()
		
	def initialiserValeurs(self):
		"""Rempli les differents formulaires avec les valeurs enregistrees"""
		#Graphismes
		self.graphismes.affichage_spinner.text = self.Config.get("Graphismes", "ScreenMode")
		self.graphismes.affichage_spinner.values = ("Fullscreen", "Borderless", "Windowed")
		self.graphismes.fonds_spinner.text = "Actif" if self.Config.getboolean("Graphismes", "FondsAnimes") else "Inactif"
		self.graphismes.fonds_spinner.values = ("Actif", "Inactif")
		self.graphismes.largeur_input.text = self.Config.get("Graphismes", "Width")
		self.graphismes.hauteur_input.text = self.Config.get("Graphismes", "Height")
		
		#Audio
		self.audio.switch_sonsActifs.active = self.Config.getboolean("Audio", "Actif")
		self.audio.general_slider.value = int(self.Config.get("Audio", "VolumeGeneral"))
		self.audio.musique_slider.value = int(self.Config.get("Audio", "VolumeMusique"))
		self.audio.effets_slider.value = int(self.Config.get("Audio", "VolumeEffets"))
		
	def enregistrer(self):
		"""Enregistre la nouvelle configuration"""
		#Graphismes
		self.Config.set("Graphismes", "ScreenMode", self.graphismes.affichage_spinner.text)
		self.Config.set("Graphismes", "FondsAnimes", self.graphismes.fonds_spinner.text == "Actif")
		self.Config.set("Graphismes", "Width", int(self.graphismes.largeur_input.text))
		self.Config.set("Graphismes", "Height", int(self.graphismes.hauteur_input.text))
		
		#Audio
		self.Config.set("Audio", "Actif", self.audio.switch_sonsActifs.active)
		self.Config.set("Audio", "VolumeGeneral", int(self.audio.general_slider.value))
		self.Config.set("Audio", "VolumeMusique", int(self.audio.musique_slider.value))
		self.Config.set("Audio", "VolumeEffets", int(self.audio.effets_slider.value))
		
		with open(config_path, 'wb') as configfile:
			self.Config.write(configfile)
			
		popup = Popup(title="Avertissement", content=Label(text="Vos preferences ont ete enregistrees.\nToutefois certains changements ne prendront effet qu'apres le redemarrage de l'application."), size_hint=(None, None), size=("600dp", "200dp"))
		popup.open()
	
	def on_open(self):
		self.etat = True
		
	def on_dismiss(self):
		self.etat = False
		
	def intInput(self, substring, from_undo=False):
		result = re.match('(\\d+)', substring)
		if result:
			self.insert_text(s, from_undo=from_undo)
		
	
class MenuDialog(Popup):
	"""Widget du menu"""
	app = ObjectProperty(None)
	title = "Menu"
	auto_dismiss = False
	
	def __init__(self, **kwargs):
		super(Popup, self).__init__(**kwargs)
		self.etat = False
		
	def on_open(self):
		self.etat = True
		
	def on_dismiss(self):
		self.etat = False
	
Game().run()